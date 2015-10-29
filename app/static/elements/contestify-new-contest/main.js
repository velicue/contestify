(function(){
  Polymer({
    is: 'contestify-new-contest',
    properties: {
      isHidden: {
        type: Boolean,
        notify: true
      },
      newContest: {
        type: Object,
        notify: true
      }
    },
    listeners: {
      'iron-form-response': 'formResponse',
      'iron-form-error': 'formError'
    },
    ready: function () {
    },
    formSubmit: function () {
      this.$.formNewContest.submit();
    },
    formHide: function () {
      this.set('isHidden', true);
    },
    formResponse: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return console.log(response.msg);
      }
      this.formHide();
      this.set('newContest', response.result);
    },
    formError: function () {
      console.log('Add Contest Failed.');
    }
  });
})();
