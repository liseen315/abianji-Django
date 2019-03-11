module.exports = function (gulp, plugin, pathConfig) {
  gulp.task('fonts', function (done) {
    gulp
      .src(pathConfig.fontPath)
      .pipe(gulp.dest(pathConfig.distRoot + 'static/fonts/'))
      .on('end', done)
  })
}
