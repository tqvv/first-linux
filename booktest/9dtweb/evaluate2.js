/**
 * Created by Administrator on 2017/10/6.
 */

var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();
page.onConsoleMessage = function (msg) {
    console.log('page title is ' + msg)
}
page.open(url,function(status){
    var title = page.evaluate(function () {
        return document.title;
    });
    console.log('Page title is' + title);
    phantom.exit();
});
