Polymer({
  is: 'contestify-feed',
  behaviors: [
    Polymer.NeonSharedElementAnimatableBehavior,
    Polymer.NeonAnimationRunnerBehavior
  ],
  properties: {
    animationConfig: {
      type: Object,
      value: function() {
        return {
          'entry': [{
            name: 'cascaded-animation',
            animation: 'transform-animation',
            transformFrom: 'translateY(100%)',
            transformTo: 'none',
            timing: {
              delay: 50
            }
          }]
        };
      }
    },
    currentGames: {
      type: Array,
    },
    newContest: {
      type: Object,
      notify: true,
      observer: 'onNewContestCreated'
    }
  },
  ready: function () {
    this.$.container.addEventListener('dom-change', function () {
      var nodeList = Polymer.dom(this.root).querySelectorAll('contestify-card');
      this.animationConfig.entry[0].nodes = Array.prototype.slice.call(nodeList);
      this.playAnimation('entry');
    }.bind(this));
  },
  toggleNewContestForm: function () {
    this.$.formNew.toggleForm();
  },
  onPublicContestListReceived: function (res) {
    this.set('currentGames', res.detail.response.result);
    console.log(this.currentGames);
  },
  onNewContestFormChanged: function () {
    if (this.isNewContestFormHidden) {
      this.$.fabAdd.setAttribute('icon', 'add');
    }
    else {
      this.$.fabAdd.setAttribute('icon', 'clear');
    }
  },
  onNewContestCreated: function () {
    this.push('currentGames', this.newContest);
  }
});
