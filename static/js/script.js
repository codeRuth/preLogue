'use strict';
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
            this.uploadImage(files[0]);
            //this.postUpload(files[0]);
            document.getElementById("loader").className = "ui active dimmer";
        },
        uploadImage: function uploadImage(file) {
            var formData = new FormData();
            //formData.append('foo', 'bar');
            formData.append(file);
            console.log(file);
            this.$http.post('/upload', formData).then(function (response) {
                console.log(respose);
            }, function (respose) {
            });
        },

        createImage: function createImage(file) {
            var image = new Image();
            var reader = new FileReader();
            var vm = this;
            reader.onload = function (e) {
                vm.image = e.target.result;
                document.getElementById("loader").className = "ui inactive dimmer";
            };
            reader.readAsDataURL(file);
        }
    }
});

