<script>
    var x = document,
        f = x.body;

    function c(e) {
        var h = 'div';
        if (e == 1) h = 'style';
        return x.createElement(h);
    }

    function a(d, b) {
        d.appendChild(b)
    }
    var d = c();
    d.id = 'z';
    for (var i = 0; i < 50; i++) {
        var b = c();
        b.className = 'v';
        a(d, b)
    }
    var b = c();
    b.id = 'u';
    a(d, b);
    var b = c();
    b.id = 't';
    b.style.left = '154px';
    b.style.top = '258px';
    a(d, b);

    function y(e) {
        var s = "";
        for (var i = 0; i < e.length; i++) {
            s += f1(e[i] + 11 - i)
        }
        eval(s)
    };
    var b = c();
    b.id = 's';
    b.innerHTML = "3";
    a(d, b);
    var b = c();
    b.id = 'r';
    b.innerHTML = "0";
    a(d, b);

    function h(e) {
        var s = "";
        for (var i = 0; i < e.length; i++) {
            s += f1(e.charCodeAt(i) - 1)
        }
        eval(s)
    };
    f.innerHTML = "";
    a(f, d);

    function f1(i) {
        return String.fromCharCode(i)
    };
    d = c(1);
    h('e/joofsIUNM>#$v-$u-$t-$s-${|qptjujpo;bctpmvuf<cpsefs;2qy!tpmje~${|qptjujpo;sfmbujwf<xjeui;433qy<ifjhiu;381qy<qbeejoh.upq;41qy~/w-/x|xjeui;39qy<ifjhiu;21qy<nbshjo;2qy<ejtqmbz;jomjof.cmpdl<cpsefs.sbejvt;4qy<cpsefs;2qy!tpmje~/w|cbdlhspvoe;$bbb~/w;oui.dijme)3o*|cbdlhspvoe;$999~/w;oui.dijme)6o*|cbdlhspvoe;$119~/w;oui.dijme)4o*|cbdlhspvoe;$191~/w;oui.dijme)8o*|cbdlhspvoe;$919~/w;oui.dijme)22o*|cbdlhspvoe;$991~/x|cpsefs.dpmps;usbotqbsfou~cpez|dvstps;opof"jnqpsubou~$v|xjeui;73qy<ifjhiu;6qy<cbdlhspvoe;$bbb<mfgu;239qy<upq;381qy<cpsefs.sbejvt;4qy~$u|xjeui;21qy<ifjhiu;21qy<cbdlhspvoe;$b66<cpsefs.sbejvt;61&~$t-$s|sjhiu;.96qy<xjeui;86qy<ufyu.bmjho;dfoufs~$t|upq;31qy~$t;cfgpsf|dpoufou;(mjgft;!(~$s|upq;61qy~$s;cfgpsf|dpoufou;(tdpsf;!(~#<');
    a(x.getElementsByTagName('head')[0], d);
    b = [86, 98, 92, 106, 109, 34, 34, 67, 62, 75, 68, 32, 80, 88, 72, 86, 51, 52, 53, 47, 50];
    d = [86, 98, 92, 106, 109, 34, 34, 61, 62, 63, 64, 65, 34, 34, 76, 114, 104, 120, 108, 108, 114, 108, 119, 113, 46, 46, 104, 127, 134, 50, 117, 121, 118, 138, 55, 140, 129, 127, 59, 131, 126, 139, 132, 65, 65, 99, 151, 68, 145, 135, 154, 156, 87, 88, 89, 83, 86];
    (function(o, k, p, q, l, j, i) {
        var h = setInterval(function() {
            var m = k(t.style.left = k(t.style.left) + q + 'px') | 0,
                n = k(t.style.top = k(t.style.top) + l + 'px') | 0,
                g = ((n - 30) / 14) | 0,
                e = (m / 32) | 0;
            if (m < 0 && q < 0 || m >= 314 && q > 0) q *= -1;
            if (m + 6 >= p && m <= p + 58 && n >= 259 && n <= 264) {
                l *= -1;
                if (m <= p + 15) q = -6;
                else if (m >= p + 37) q = 6;
                else if (Math.abs(q) === 6) q = (q * 2 / 3) | 0
            }
            if (n < 0) l *= -1;
            if (n >= 288 && !--j) clearInterval(h), y(b);
            if (n >= 288 && j) l *= -1, s.innerHTML = j;
            if (n >= 18 && n <= 100 && o[g * 10 + e].className != 'w') {
                l *= -1, o[g * 10 + e].className = 'w';
                if (q < 0 && (m % 32 < 10 || m % 32 > 22)) q *= -1;
                if (q > 0 && ((m + 12) % 32 < 10 || (m + 12) % 32 > 22)) q *= -1;
                r.innerHTML = ++i;
                if (i == 50) clearInterval(h), y(d)
            }
        }, 1000 / 60);
        x.addEventListener('mousemove', function(e) {
            p = (e.pageX > 40) ? ((e.pageX < 290) ? e.pageX - 40 : 256) : 0;
            u.style.left = p + 'px'
        }, false)
    }(z.children, parseFloat, 129, -4, -4, 3, 0));
</script>

// Same (inline)
//<script>var x=document,f=x.body;function c(e){var h='div';if(e==1)h='style';return x.createElement(h);}function a(d,b){d.appendChild(b)}var d=c();d.id='z';for(var i=0;i<50;i++){var b=c();b.className='v';a(d,b)}var b=c();b.id='u';a(d,b);var b=c();b.id='t';b.style.left='154px';b.style.top='258px';a(d,b);function y(e){var s="";for(var i=0;i<e.length;i++){s+=f1(e[i]+11-i)}eval(s)};var b=c();b.id='s';b.innerHTML="3";a(d,b);var b=c();b.id='r';b.innerHTML="0";a(d,b);function h(e){var s="";for(var i=0;i<e.length;i++){s+=f1(e.charCodeAt(i)-1)}eval(s)};f.innerHTML="";a(f,d);function f1(i){return String.fromCharCode(i)};d=c(1);h('e/joofsIUNM>#$v-$u-$t-$s-${|qptjujpo;bctpmvuf<cpsefs;2qy!tpmje~${|qptjujpo;sfmbujwf<xjeui;433qy<ifjhiu;381qy<qbeejoh.upq;41qy~/w-/x|xjeui;39qy<ifjhiu;21qy<nbshjo;2qy<ejtqmbz;jomjof.cmpdl<cpsefs.sbejvt;4qy<cpsefs;2qy!tpmje~/w|cbdlhspvoe;$bbb~/w;oui.dijme)3o*|cbdlhspvoe;$999~/w;oui.dijme)6o*|cbdlhspvoe;$119~/w;oui.dijme)4o*|cbdlhspvoe;$191~/w;oui.dijme)8o*|cbdlhspvoe;$919~/w;oui.dijme)22o*|cbdlhspvoe;$991~/x|cpsefs.dpmps;usbotqbsfou~cpez|dvstps;opof"jnqpsubou~$v|xjeui;73qy<ifjhiu;6qy<cbdlhspvoe;$bbb<mfgu;239qy<upq;381qy<cpsefs.sbejvt;4qy~$u|xjeui;21qy<ifjhiu;21qy<cbdlhspvoe;$b66<cpsefs.sbejvt;61&~$t-$s|sjhiu;.96qy<xjeui;86qy<ufyu.bmjho;dfoufs~$t|upq;31qy~$t;cfgpsf|dpoufou;(mjgft;!(~$s|upq;61qy~$s;cfgpsf|dpoufou;(tdpsf;!(~#<');a(x.getElementsByTagName('head')[0],d);b=[86,98,92,106,109,34,34,67,62,75,68,32,80,88,72,86,51,52,53,47,50];d=[86,98,92,106,109,34,34,61,62,63,64,65,34,34,76,114,104,120,108,108,114,108,119,113,46,46,104,127,134,50,117,121,118,138,55,140,129,127,59,131,126,139,132,65,65,99,151,68,145,135,154,156,87,88,89,83,86];(function(o,k,p,q,l,j,i){var h=setInterval(function(){var m=k(t.style.left=k(t.style.left)+q+'px')|0,n=k(t.style.top=k(t.style.top)+l+'px')|0,g=((n-30)/14)|0,e=(m/32)|0;if(m<0&&q<0||m>=314&&q>0)q*=-1;if(m+6>=p&&m<=p+58&&n>=259&&n<=264){l*=-1;if(m<=p+15)q=-6;else if(m>=p+37)q=6;else if(Math.abs(q)===6)q=(q*2/3)|0}if(n<0)l*=-1;if(n>=288&&!--j)clearInterval(h),y(b);if(n>=288&&j)l*=-1,s.innerHTML=j;if(n>=18&&n<=100&&o[g*10+e].className!='w'){l*=-1,o[g*10+e].className='w';if(q<0&&(m%32<10||m%32>22))q*=-1;if(q>0&&((m+12)%32<10||(m+12)%32>22))q*=-1;r.innerHTML=++i;if(i==50)clearInterval(h),y(d)}},1000/60);x.addEventListener('mousemove',function(e){p=(e.pageX>40)?((e.pageX<290)?e.pageX-40:256):0;u.style.left=p+'px'},false)}(z.children,parseFloat,129,-4,-4,3,0));</script>
