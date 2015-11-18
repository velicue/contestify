(function(){
  Polymer({
    is: 'contestify-contest',
    properties: {
      contestInfo : {
        type: Object,
        notify: true,
        observer: 'refresh'
      },
      matchList: {
        type: Array,
        value: [],
        notify: true
      },
      graph: {
        type: Array,
        value: []
      },
      isAdmin: {
        type: Boolean,
        value: false
      }
    },
    ready: function () {
      this.addEventListener('put-score', function (e) {
        this.$.ajaxPutScore.url = '/match/' + e.detail.matchId;
        this.$.dialogPutScore.toggle();
      });
    },
    hardRefresh: function () {
      this.set('matchList', []);
      this.$.ajaxMatchList.params = {'id': this.contestInfo._id.$oid};
      this.$.ajaxGraph.params = {'id': this.contestInfo._id.$oid};
      this.$.ajaxMatchList.generateRequest();
      this.$.ajaxGraph.generateRequest();
    },
    refresh: function () {
      if (!this.contestInfo._id) {
        return;
      }
      this.$.inputId.value = this.contestInfo._id.$oid;
      this.$.ajaxMatchList.params = {'id': this.contestInfo._id.$oid};
      this.$.ajaxGraph.params = {'id': this.contestInfo._id.$oid};
      this.$.ajaxMatchList.generateRequest();
      this.$.ajaxGraph.generateRequest();
      this.$.ajaxCurrentUser.generateRequest();
    },
    putScoreSubmit: function () {
      if (this.$.formPutScore.validate()) {
        var toSend = {};
        toSend.score1 = +this.$.formPutScore.score1.value;
        toSend.score2 = +this.$.formPutScore.score2.value;
        toSend.contestId = this.$.formPutScore.contestId.value;
        this.$.ajaxPutScore.body = toSend;
        this.$.ajaxPutScore.generateRequest();
        this.$.dialogPutScore.toggle();
      }
    },
    joinCurrentContest: function () {
      this.$.ajaxJoin.url = '/playerList/' + this.contestInfo._id.$oid;
      this.$.ajaxJoin.body = {
        userId: this.currentId
      };
      this.$.ajaxJoin.generateRequest();
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    },
    onJoinReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      this.hardRefresh();
      this.$.dialogJoin.toggle();
    },
    onMatchListReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      this.set('matchList', response.result.matches.map(function (e) {
        return e.$oid;
      }));
    },
    onGraphReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      response.result.items.sort(function (m, n) {
        return n.totalPoints - m.totalPoints;
      });
      this.set('graph', response.result.items);
      console.log(response.result.items);
    },
    onCurrentUserReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      this.set('currentId', response.result.currentUserId);
      this.set('isAdmin', this.currentId === this.contestInfo.adminId.$oid);
    }
  });
})();
