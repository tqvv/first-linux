/**
 * Created by Administrator on 2017/10/6.
 */
var page = require('webpage').create();
/*缩放功能好像不能用
page.viewportSize ={width:950,height:4953};
page.clipRect = {top:0,left:0,width:512,hgight:256};
*/

page.open('http://www.cnblogs.com/qiyeboy',function(status)
{
    console.log("Status:" + status);
if (status ==='success')
{
page.render('qiye_xiao.png');
}
     phantom.exit();
});
