const postcss = require('gulp-postcss')
const atImport = require('postcss-import')

module.exports = function (gulp, plugin, pathConfig) {
  let processors = [atImport]
  gulp.task('scss', function (done) {
    gulp
      .src(pathConfig.scssPath)
      .pipe(plugin.gulpPlumber())
      .pipe(postcss(processors))
      .pipe(
        plugin
          .gulpSass({ outputStyle: 'compressed' })
          .on('error', plugin.gulpSass.logError)
      )
      .pipe(
        plugin.autoprefixer({
          browsers: ['last 2 versions'],
          cascade: false
        })
      )
      .pipe(
        plugin.cssnano({
          safe: true
        })
      )
      .pipe(gulp.dest(pathConfig.distRoot + 'static/styles/'))
      .on('end', done)
  })
}
