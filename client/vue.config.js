const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
     proxy: 'http://47.254.248.134:5000'
 }
})
