var o_a = require("crypto-js"); // npm install crypto-js

var l = {
    key: o_a.enc.Utf8.parse("*****"),
    iv: o_a.enc.Utf8.parse(function(t) {
        for (var e = "", i = 0; i < t.length - 1; i += 2) {
            var n = parseInt(t[i] + "" + t[i + 1], 16);
            e += String.fromCharCode(n)
        }
        return e
    }("*****"))
}
var tf = function(e) {
    return typeof e
}
var f = function(t) {
    var e = "";
    return Object.keys(t).sort().forEach((function(n) {
        e += n + ("object" === tf(t[n]) ? JSON.stringify(t[n], (function(t, e) {
            return "number" == typeof e && (e = String(e)),
            e
        }
        )).replace(/\//g, "\\/") : t[n])
    }
    )),
    e
}
var d = function(data) {
    return o_a.MD5(data).toString(); // 技巧. 这个先不动
}

var v = function(data) {
    return function(data) {
        return o_a.AES.encrypt(data, l.key, {
            iv: l.iv,
            mode: o_a.mode.CBC,
            padding: o_a.pad.Pkcs7
        }).toString()
    }(data)
}
function f_a(t){
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
      , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "*****"
      , n = e + f(data) + f(t) + e;
    return n = d(n),
    n = v(n)
}

function fn(L){
    // 复制粘贴
    var tm = parseInt((new Date).getTime() / 1e3) + ""; // 通过错误判断这里要处理成字符串
    var U = {
        "App-Ver": "",
        "Os-Ver": "",
        "Device-Ver": "",
        "Imei": "",
        "Access-Token": "",
        "Timestemp": tm,
        "NonceStr": "".concat(tm).concat('*****'),
        "App-Id": "*****",
        "Device-Os": "web"
    }
    // 输入的所有参数. 网站的参数
    // 从python传递过来
    // var L = {
    //     "username": "18811131111",
    //     "password": "11111111",
    //     "code": "fads",
    //     "hdn_refer": ""
    // }

    var ret = f_a(U, L, '*****');

    U.Signature = ret;
    U.CHOST = "*****";

    return U;
}

// console.log(f)
// 找l的方法
// 1. 按照webpack的方案一步一步搜
// 2. 直接搜该值
// 3. 有些特殊的属性是通过get返回的. 我们可以直接找到get函数.

// 抠代码逻辑: 缺啥,抠啥
