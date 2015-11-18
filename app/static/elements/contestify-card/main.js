(function() {
  'use strict';

  Polymer({
    is: 'contestify-card',
    properties: {
      matchId: String,
      matchAdminId: String,
      matchTitle: String,
      matchDescription: String,
      matchFormat: String,
      matchGame: String,
      matchTotal: Number,
      matchCurrent: Number,
      matchAdmin: Object,
    },
    ready: function () {
      this.$.ajaxUserDetail.url = '/user?id=' + this.matchAdminId;
      this.$.ajaxUserDetail.generateRequest();
    },
    onCardTaped: function () {
      page('/contest/' + this.matchId);
    },
    onUserDetailReceived: function (res) {
      var response = res.detail.response;
      if ('OK' !== response.status) {
        return this.showFailMsg(response.msg);
      }
      this.set('matchAdmin', response.result);
      this.set('matchAdmin.name', response.result.firstName + ' ' + response.result.lastName);
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
