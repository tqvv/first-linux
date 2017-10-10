/**
 * Created by Administrator on 2017/10/6.
 */
vat url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();
page.onResourceRequested=function (request) {
    console.log('request'+JSON.stringify(request,undefined,4));
};
page.onResourceRequested=function (response) {
    console.log('Receive' + JSON.stringify(response,undefined,4));
};
page.open(url);
