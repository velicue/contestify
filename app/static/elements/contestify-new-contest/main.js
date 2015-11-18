(function(){
  Polymer({
    is: 'contestify-new-contest',
    properties: {
      newContest: {
        type: Object,
        notify: true
      },
      isHidden: {
        type: Boolean,
        notify: true,
      }
    },
    listeners: {
      'iron-form-response': 'formResponse',
      'iron-form-error': 'formError'
    },
    ready: function () {
    },
    formSubmit: function () {
      if (this.$.formNewContest.validate()) {
        this.$.formNewContest.submit();
      }
    },
    toggleForm: function () {
      this.$.formNew.toggle();
    },
    formResponse: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      this.$.formNew.close();
      this.set('newContest', response.result);
    },
    formError: function () {
        return this.showFailMsg('Create new contest error!');
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
