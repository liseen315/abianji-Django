const gulp = require('gulp')
const gulpLoadPlugins = require('gulp-load-plugins')
const pathConfig = require('./workflow/pathConfig')
const requireDir = require('require-dir')
const clean = require('del')

gulpLoadPlugins.hashAssets = require('gulp-md5-assets')
gulpLoadPlugins.imagemin = require('gulp-imagemin')
gulpLoadPlugins.gulpSass = require('gulp-sass')
gulpLoadPlugins.gulpPlumber = require('gulp-plumber')
gulpLoadPlugins.autoprefixer = require('gulp-autoprefixer')
gulpLoadPlugins.cssnano = require('gulp-cssnano')

requireDir('./workflow/tasks/', {
  mapKey: function (value, baseName) {
    value(gulp, gulpLoadPlugins, pathConfig)
  }
})

gulp.task('watch', function () {
  gulp.watch(pathConfig.scssPath, ['scss'])
})

gulp.task('del', function () {
  return clean(['public/static/**/*'], { force: true })
})

gulp.task('release', ['hash:css', 'hash:js'])

gulp.task('default', ['image', 'scss', 'watch', 'watchJS'])

