const path = require('path')
const glob = require('glob')
const log = require('fancy-log')
/**
 * 多入口目录拆分
 * @param {*} dir  目标目录
 * @param {*} ext  文件后缀
 */
module.exports = function (dir, ext) {
  let files = glob.sync('./' + dir + '/**/*.' + ext, {
    ignore: './src/scripts/_vue/**/*'
  })
  let res = {}
  files.forEach(function (file) {
    let relativePath = path.relative(dir, file)
    let relativeName = relativePath.slice(0, relativePath.lastIndexOf('.'))
    res[relativeName] = './' + relativePath
  })

  if (JSON.stringify(res) === '{}') {
    log('脚本目录为空,webpack不会进行脚本打包')
    return false
  }
  return res
}
