const path = require('path')
const getEntry = require('./workflow/common/getEntry')
const webpack = require('webpack')

// 后续需要插件需要在这个方法内实现
let getPlugins = function (env) {
  let pluginList = [
    new webpack.DllReferencePlugin({
      context: __dirname,
      manifest: require('./blog/static/scripts/vendors.manifest.json')
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }),
  ]
  return pluginList
}

module.exports = function (env, pathConfig) {
  let entrys = getEntry(pathConfig.sourceRoot + 'scripts', 'js')
  if (!entrys) {
    return false
  }
  return {
    context: path.resolve(__dirname, 'src/scripts/'),
    entry: entrys,
    output: {
      filename: '[name].js',
      pathinfo: false,
      path: path.resolve(__dirname, pathConfig.distRoot + 'static/scripts')
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: '/node_modules/',
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
              cacheDirectory: true // 开缓存会降150+ms
            }
          }
        }
        // 后期再考虑vue组件内的样式绑定,多入口要考虑抽取样式等一系列逻辑
      ]
    },
    mode: env,
    devtool: env === 'production' ? 'none' : 'cheap-module-eval-source-map',
    plugins: getPlugins(env),
    resolve: {
      extensions: ['.scss', '.js', '.json'],
      alias: {
        utils$: path.resolve(__dirname, 'src/scripts/utils/util.js')
      }
    },
    performance: {
      hints: false,
      maxEntrypointSize: 400000,
      assetFilter: function (assetFilename) {
        return assetFilename.endsWith('.js')
      }
    }
  }
}
