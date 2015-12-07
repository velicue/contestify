(function () {
  Polymer({
    is: 'contestify-match',
    properties: {
      matchId: {
        type: String,
        value: null,
        observer: 'refresh'
      },
      matchDetail: {
        type: Object
      },
      isAdmin: {
        type: Boolean,
        value: false
      }
    },
    refresh: function () {
      if (!this.matchId) {
        return;
      }
      this.$.ajaxMatchDetail.params = {'id': this.matchId};
      this.$.ajaxMatchDetail.generateRequest();
    },
    putScore: function () {
      this.fire('put-score', {matchId: this.matchDetail._id.$oid});
    },
    onMatchDetailReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      response.result.score1 = -1 === response.result.score1 ? '' : response.result.score1;
      response.result.score2 = -1 === response.result.score2 ? '' : response.result.score2;
      this.set('matchDetail', response.result);
      this.$.ajaxUserDetail.params = {'id': this.matchDetail.player1Id.$oid};
      this.$.ajaxUserDetail.generateRequest();
      this.$.ajaxUserDetail.params = {'id': this.matchDetail.player2Id.$oid};
      this.$.ajaxUserDetail.generateRequest();
    },
    onUserDetailReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      if (response.result._id.$oid === '5664f1020207406600de67f0') {
        // BYE
        this.remove();
      }
      else if (response.result._id.$oid === this.matchDetail.player1Id.$oid) {
        this.set('matchDetail.player1Id.name', response.result.firstName + ' ' + response.result.lastName);
        this.set('matchDetail.player1Id.initial', response.result.firstName[0].toUpperCase() + response.result.lastName[0].toUpperCase());
      }
      else if (response.result._id.$oid === this.matchDetail.player2Id.$oid) {
        this.set('matchDetail.player2Id.name', response.result.firstName + ' ' + response.result.lastName);
        this.set('matchDetail.player2Id.initial', response.result.firstName[0].toUpperCase() + response.result.lastName[0].toUpperCase());
      }
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
