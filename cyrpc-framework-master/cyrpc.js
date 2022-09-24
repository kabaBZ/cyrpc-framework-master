!function (a) {

    new Promise((e, s) => {
            e(a)
        }
    ).then((cbbiyhh) => {
            var cbb_MyId = "1001";
            var cbb_vvnn = WebSocket;
            ws = new cbb_vvnn("ws://127.0.0.1:5679/cbb");
            console.log("10id")
            ws.onopen = function () {
                console.log("11id")
                ws.send(cbb_MyId+"---");
            }
            ;
            ws.onmessage = function (evt) {
                if (evt.data == 'c~c') {
                    console.log('pp')
                    ws.send(cbb_MyId+'---'+'c~c')
                    return;
                }
                console.log('传入数据: ' + evt.data);
                var data = [];
                if (evt.data.length == 0) {
                    data.push(cbbiyhh());
                    ws.send(JSON.stringify(data))
                    data = []
                } else {
                    var typeOfDate = evt.data[0];
                    switch (typeOfDate) {
                        case "A":
                            var dataInfo = JSON.parse(evt.data.slice(1));
                            data.push(cbbiyhh(dataInfo));
                            break
                        case "O":
                            var dataInfo = JSON.parse(evt.data.slice(1))
                            data.push(cbbiyhh(dataInfo));
                            break
                        case "S":
                            data.push(cbbiyhh(evt.data.slice(1)));
                            break
                        case "I":
                            data.push(cbbiyhh(parseInt(evt.data.slice(1))));
                            break
                    }
                    ;
                    console.log(cbb_MyId+'---'+JSON.stringify(data));
                    ws.send(cbb_MyId+'---'+JSON.stringify(data));
                    data = []
                }
                ;
            }
            ;
            ws.onclose = function () {
                console.log("rpc已经断开了哦");
            };
            ws.onerror = function () {
                console.log("rpc已经断开了哦");
            };

        }
    )
    ;
}(nn)