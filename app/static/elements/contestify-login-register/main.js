(function(){
  Polymer({
    is: 'contestify-login-register',
    properties: {
      sectionIndex: {
        type: Number,
        value: 0,
        notify: true
      },
      isHidden: {
        type: Boolean,
        value: true,
        notify: true
      },
      formInfo: {
        type: Object,
        notify: true
      }
    },
    ready: function () {
    },
    hide: function () {
      this.set('isHidden', true);
    },
    show: function () {
      this.set('isHidden', false);
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
      }
      else {
        // login
        if (this.isLoginFormInvalid()||this.isLoginFormEmpty()) {
          return;
        }
        obj.email = this.$.inputEmailLogin.value;
        obj.password = this.$.inputPasswordLogin.value;
        this.set('formInfo', obj);
      }
    }
  });
})();
