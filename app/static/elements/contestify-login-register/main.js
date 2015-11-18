(function(){
  Polymer({
    is: 'contestify-login-register',
    properties: {
      sectionIndex: {
        type: Number,
        value: 0,
        notify: true
      },
      formInfo: {
        type: Object,
        notify: true
      },
      isLoginRegister: {
        type: Boolean,
        value: false,
        notify: true
      },
      currentUser: {
        type: Object,
        value: {},
        notify: true
      }
    },
    ready: function () {
    },
    hide: function () {
      this.$.formLogin.close();
    },
    getCurrentUserDetail: function () {
      this.$.ajaxUserDetail.params = {'id': this.currentUser.userId};
      this.$.ajaxUserDetail.generateRequest();
    },
    logoutCurrentUser: function () {
      this.$.ajaxLogout.generateRequest();
    },
    isRegisterFormInvalid: function () {
      return this.$.inputEmailRegister.invalid ||
          this.$.inputFirstRegister.invalid ||
          this.$.inputLastRegister.invalid ||
          this.$.inputPasswordRegister.invalid;
    },
    isRegisterFormEmpty: function () {
      return this.$.inputEmailRegister.value === '' &&
          this.$.inputFirstRegister.value === '' &&
          this.$.inputLastRegister.value === '' &&
          this.$.inputPasswordRegister.value === '';
    },
    isLoginFormInvalid: function () {
      return this.$.inputEmailLogin.invalid ||
        this.$.inputPasswordLogin.invalid;
    },
    isLoginFormEmpty: function () {
      return this.$.inputEmailLogin.value === '' &&
        this.$.inputPasswordLogin.value === '';
    },
    toggleLoginRegister: function () {
      this.$.formLogin.toggle();
    },
    submit: function () {
      var obj = {};
      if (this.sectionIndex === 0) {
        // register
        if (this.isRegisterFormInvalid()||this.isRegisterFormEmpty()) {
          return;
        }
        obj.email = this.$.inputEmailRegister.value;
        obj.password = this.$.inputPasswordRegister.value;
        obj.firstName = this.$.inputFirstRegister.value;
        obj.lastName = this.$.inputLastRegister.value;
        this.set('formInfo', obj);
        this.$.ajaxRegister.generateRequest();
      }
      else {
        // login
        if (this.isLoginFormInvalid()||this.isLoginFormEmpty()) {
          return;
        }
        obj.email = this.$.inputEmailLogin.value;
        obj.password = this.$.inputPasswordLogin.value;
        this.set('formInfo', obj);
        this.$.ajaxLogin.generateRequest();
      }
    },
    onCurrentUserReceived: function (res) {
      var response = res.detail.response;
      console.log(response);
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      var currentId = response.result.currentUserId;

      this.set('isLoginRegister', currentId !== null);
      if (currentId) {
        this.set('currentUser.userId', currentId);
        this.getCurrentUserDetail();
      }
    },
    onLogoutReceived: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      this.set('isLoginRegister', false);
    },
    onUserDetailReceived: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      this.set('currentUser.firstName', response.result.firstName);
      this.set('currentUser.lastName', response.result.LastName);
    },
    onRegisterReceived: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      this.toggleLoginRegister();
      this.$.ajaxLogin.generateRequest();
    },
    onLoginReceived: function (res) {
      var response = res.detail.response;
      if (response.status === 'Failed') {
        return this.showFailMsg(response.msg);
      }
      if (this.$.formLogin.opened) {
        this.toggleLoginRegister();
      }
      this.$.ajaxCurrentUser.generateRequest();
    },
    parse: function(obj) {
      return JSON.stringify(obj);
    },
    showFailMsg: function (msg) {
      this.fire('contestify-toast-msg', {text: msg});
    }
  });
})();
