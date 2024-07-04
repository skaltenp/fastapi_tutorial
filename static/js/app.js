const App = {
    data() {
        return {
            results_classification: [],
            results_object_detection: []
        }
    },
    methods: {
        onFileSelected: function (event) {
            let thisref = this;
            let post_url = "http://localhost:8000/img";
            let request_method = "POST";
            let form_data = new FormData();
            form_data.append('image_file', event.target.files[0]);
            form_data.append('api_key', "d2ad67989fc0dfb80672be820e8f0ca263a07541ab805b05e46de8a759879eac")
            form_data.append('api_secret', "09c8ee34fd943c30ce6a00a55f8ebbf22bf9f3864b4d2e70120afc23837f7d4d")
            $.ajax({
                type: request_method,
                url: post_url,
                data: form_data,
                cache: false,
                contentType: false,
                processData: false,
                success: function(response){
                    
                },
            });
        }
    },
}
const app = Vue.createApp(App);
app.mount('#result-list');