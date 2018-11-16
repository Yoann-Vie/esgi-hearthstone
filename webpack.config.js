
var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',
    context: __dirname,
    entry: './assets/scripts/main',
    output: {
        path: path.resolve('./assets/webpack_bundles/'),
        filename: "[name].js"
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ]
}
