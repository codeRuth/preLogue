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
            log('on' + event.type);
        }
    }

    reco.onerror = function (e) {
        console.log('onerror ' + e.error);
    };

    reco.onresult = function (e) {
        try {
            console.log('onresult ' + res2str(e.results, e.resultIndex));
        } catch (ex) {
            console.log('onresult - exception');
        }
    };

    if (reco.onresults != undefined) {
        console.log('onresults exists');
    }
    console.log('created recognition object');
}

function start() {
    log('start()');
    reco.lang = document.getElementById('lang').value;
    reco.continuous = document.getElementById('continuous').checked;
    reco.interimResults = document.getElementById('interim').checked;
    log('reco.lang = ' + reco.lang);
    log('reco.continuous = ' + reco.continuous);
    log('reco.interimResults = ' + reco.interimResults);
    try {
        reco.start();
    } catch (e) {
        log('exception: ' + e);
    }
}

function stop() {
    log('stop()');
    reco.stop();
}

function abort() {
            log('abort()');
            reco.abort();
        }