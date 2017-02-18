/**
 * Created by coderuth on 2/17/2017.
 */

function setup() {
    try {
        window.reco = new webkitSpeechRecognition();
    } catch (e) {
        console.log("The Web Speech API is not supported by this browser.");
        return;
    }
    reco.maxAlternatives = 25;
    for (var prop in reco) {
        if (!prop.match('^on'))
            continue;
        reco[prop] = function () {
            console.log('on' + event.type);
        }
    }
    reco.onerror = function (e) {
        console.log('onerror ' + e.error);
    };
    reco.onresult = function (e) {
        try {
            console.log('onresult ' + res2str(e.results, e.resultIndex));
            // res2str(e.results, e.resultIndex);
        } catch (ex) {
            console.log('onresult - exception');
        }
    };
    if (reco.onresults != undefined)
        console.log('onresults exists');
    console.log('created recognition object');
}

function start() {
    console.log('start()');
    //reco.lang = document.getElementById('lang').value;
    reco.continuous = document.getElementById('continuous').checked;
    //reco.interimResults = document.getElementById('interim').checked;
    //console.log('reco.lang = ' + reco.lang);
    console.log('reco.continuous = ' + reco.continuous);
    //console.log('reco.interimResults = ' + reco.interimResults);
    try {
        reco.start();
    } catch (e) {
        console.log('exception: ' + e);
    }
}

function stop() {
    console.log('stop()');
    reco.stop();
}

function res2str(results, index) {
    // var JSONObj = {};
    // var jsonArr = [];
    //
    // JSONObj.property = index;
    // JSONObj.anotherProp = [];
    // for (r in results[index]) {
    //     JSONObj.anotherProp.push(r);
    //
    //
    //     jsonArr.push({
    //         text: r.,
    //         confidence:
    //     });
    // }

    // var json = JSON.stringify(myObject);
    // var s = index + ":{";
    // var r = results[index];
    // if (r.isFinal)
    //     s += '(final) ';
    // s += '[';
    // for (var j = 0; j < r.length; ++j) {
    //     s += r.item(j).transcript + ' (' + r.item(j).confidence + ')';
    //     if (j < r.length - 1)
    //         s += ',';
    // }
    // s += ']';
    // s += "}";

    return results[index].item(0).transcript.toString();
}

function abort() {
    console.log('abort()');
    reco.abort();
}