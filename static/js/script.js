/**
 * Created by coderuth on 4/15/2017.
 */
'use strict';

function HandleBrowseClick() {
    var fileinput = document.getElementById("browse");
    fileinput.click();
    var textinput = document.getElementById("filename");
    textinput.value = fileinput.value;
}

var app = new Vue({
    el: '#app',
    data: {
        image: ''
    },
    methods: {
        onFileChange: function onFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length) return;
            this.createImage(files[0]);
        },
        createImage: function createImage(file) {
            var image = new Image();
            var reader = new FileReader();
            var vm = this;

            reader.onload = function(e) {
                vm.image = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }
});

