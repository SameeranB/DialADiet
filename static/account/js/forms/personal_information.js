const app = new Vue(
    {
        delimiters: ['[[', ']]'],
        el: '#content',
        data: {
            pageTitle: '<span class="first-word"> P</span>ersonal <span class="second-word">I</span>nformation',

            questionTitles: {
                1: 'Let\'s get the basics out of the way, shall we?'
            },

            questionSubTitles: {
                1: 'Your Profile Picture should be a good place to start.\n'
            },

            answerInputs: {
                1: '  <img alt="Upload Profile Picture" class="profile-pic"\n' +
                    '                 src="{% static \'account/Assets/forms/personal_info/profile_pic.svg\' %}">\n' +
                    '            <img alt="Upload Profile Picture" class="profile-pic-hover"\n' +
                    '                 src="{% static \'account/Assets/forms/personal_info/profile_pic_hover.svg\' %}">\n' +
                    ''
            },

            answerOptions: {
                1: '            <div class="option-no-profile-pic">\n' +
                    '                    No, I don\'t want a profile picture.\n' +
                    '            </div>\n' +
                    '\n' +
                    '            <div class="option-confirm-profile-pic">\n' +
                    '                Yes this looks good. Let\'s move on...\n' +
                    '            </div>'
            },
            questionNumber: 1

        },

        computed: {
            currentTitle: function () {
                console.log(this.pageTitle)
                return this.pageTitle;
            },

            currentQuestionTitle: function () {
                console.log(this.questionTitles[this.questionNumber])
                return this.questionTitles[this.questionNumber];
            },

            currentQuestionSubtitle: function () {
                console.log(this.questionSubTitles[this.questionNumber])
                return this.questionSubTitles[this.questionNumber];
            },

            currentAnswerInput: function () {
                console.log(this.answerInputs[this.questionNumber])
                return this.answerInputs[this.questionNumber];
            },

            currentAnswerOptions: function () {
                console.log(this.answerOptions[this.questionNumber])
                return this.answerOptions[this.questionNumber]
            }

        },

        methods: {
            nextQuestion: function () {

                if (this.questionNumber !== 15) {
                    this.questionNumber++
                }
            },

            previousQuestion: function () {
                if (this.questionNumber !== 1) {
                    this.questionNumber--
                }
            }

        }
    }
)