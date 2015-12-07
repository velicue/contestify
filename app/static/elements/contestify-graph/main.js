(function () {
  Polymer({
    is: 'contestify-graph',
    properties: {
      graphDetail: {
        type: Object,
        value: null,
        observer: 'refresh'
      },
      graphInitial: String
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
      this.set('graphDetail.name', response.result.firstName.toUpperCase() + ' ' + response.result.lastName.toUpperCase());
      this.set('graphInitial', response.result.firstName[0].toUpperCase() + response.result.lastName[0].toUpperCase());
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
