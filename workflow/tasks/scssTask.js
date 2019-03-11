const postcss = require('gulp-postcss')
const atImport = require('postcss-import')
module.exports = function (gulp, plugin, pathConfig) {
  // let processors = [atImport, require('postcss-scss')]

  function callback (file) {
    return {
      plugins: [
        require('postcss-import'),
      ],
      options: {
        parser: require('postcss-scss')
      }
    }
  }

  gulp.task('scss', function (done) {
    gulp
      .src(pathConfig.scssPath)
      .pipe(plugin.gulpPlumber())
      .pipe(postcss(callback))
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
