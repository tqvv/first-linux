/**
 * Created by Administrator on 2017/10/6.
 */
var page = require('webpage').create();
console.log('The defaute user agent is' + page.settings.userAgent);
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0';

page.open('http://movie.mtime.com/108737/',function(status){
    if (status !== 'success'){
        console.log('unable to access network');
    }else{
        var ua = page.evaluate(function () {
            return document.getElementById('ratingRegion').textContent;
        })
        console.log(ua)
    }
    phantom.exit();
})