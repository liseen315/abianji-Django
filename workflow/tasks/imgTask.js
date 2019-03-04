module.exports = function (gulp, plugin, pathConfig) {
  gulp.task('image', function (done) {
    gulp
      .src(pathConfig.imgPath)
      .pipe(gulp.dest(pathConfig.distRoot + 'static/images/'))
      .on('end', done)
  })
}
