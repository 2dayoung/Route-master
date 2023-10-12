const express = require('express');
const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const app = express();

//포트설정
app.set('port', process.env.PORT || 8080);

//공통미들웨어
app.use(express.static(__dirname + '/public'));
app.use(morgan('dev'));
app.use(cookieParser('secret@1234'));   //암호화된 쿠키를 사용하기 위한 임의의 문자 전송
app.use(session({
    secret : 'secret@1234',     //암호화
    resave : false,             //새로운 요청 시 세션에 변동 사항이 없어도 다시 저장할지 설정
    saveUninitialized : true,   //세션에 저장할 내용이 없어도 저장할지 설정
    cookie: {                   //세션 쿠키 옵션들 설정  httpOnly, expires, domain, path, secure, sameSite
        httpOnly : true,        //로그인 구현 시 필수 적용, 자바스크리븥로 접근 할 수 없게 하는 기능
    },
    
}));
app.use(express.json());
app.use(express.urlencoded({extended: true}));


//라우팅 설정
app.get('/', (req,res) => {
    if (req.session.name) {
        const output = `
        <h2>로그인한 사용자님</h2><br>
        <p>${req.session.name}님 안녕하세요.</p><br>
        `
        res.send(output);
        // res.sendFile(__dirname + '/index.html');
    } else{
        // const output = `
        
        // <h2>로그인하지 않은 사용자입니다</h2><br>
        // <p>로그인해 주세요.</p><br>
        // `
        // res.send(output);
        res.sendFile(__dirname + '/index.html');
    }
});

app.get('/map', (req,res) => {

    res.sendFile(__dirname + '/index.html');
    
});

// app.get('/login', (req, res) => {
//     console.log(req.session);
//     req.session.name = '로드북';
//     res.end('Login OK')
// });

// app.get('/logout',  (req, res) => {
//     res.clearCookie('connect.sid')//세션쿠키삭제
//     res.end('Logout OK');
// });

//서버포트와 연결
app.listen(app.get('port'), () => {
    console.log(app.get('port'), "번 포트np에서 실행 중, ,  ")
});