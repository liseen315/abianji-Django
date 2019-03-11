import hljs from 'highlight.js'

class Abianji {
  constructor () {
    this.J_toggler = $('#J_toggler')
    this.J_nav = $('#J_nav')

    this.init()
  }

  init() {
    this.J_toggler.on('click',event => {
      $("nav").slideToggle();
    })
  }
}

new Abianji()

hljs.initHighlightingOnLoad()

