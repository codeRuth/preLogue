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
            console.log('onresult ' + getResult(e.results, e.resultIndex));
            doSend(getResult(e.results, e.resultIndex));
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
    reco.continuous = document.getElementById('continuous').checked;
    console.log('reco.continuous = ' + reco.continuous);
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

function getResult(results, index) {
    return results[index].item(0).transcript.toString();
}

function abort() {
    console.log('abort()');
    reco.abort();
}