(function () {
  Polymer({
    is: 'contestify-graph',
    properties: {
      graphDetail: {
        type: Object,
        value: null,
        observer: 'refresh'
      }
    },
    refresh: function () {
      this.$.ajaxUserDetail.params = {'id': this.graphDetail.playerId.$oid};
      this.$.ajaxUserDetail.generateRequest();
    },
    onUserDetailReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      this.set('graphDetail.name', response.result.firstName + ' ' + response.result.lastName);
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
