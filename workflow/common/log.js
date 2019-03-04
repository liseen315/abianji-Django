const gulpColor = require('gulp-color')
const fancyLog = require('fancy-log')
module.exports = function (msg, color) {
  fancyLog(gulpColor(msg, color))
}
