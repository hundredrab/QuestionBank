var show = new Vue({
    el: '#show',
    data: {
        qset: "hello",
        status: "...",
    },
    mounted(){
        this.populateQset()
    },
    methods: {
        populateQset: _.debounce(function(){
            var app = this
            this.status = "Refreshing..."
            axios.get(
                "http://127.0.0.1:8000/question/api/set/"+(id), {
                }
            ).then(function (response) {
                console.log(response.data)
                app.qset = response.data
                app.status = "Found " + app.qset.length + " questions."
            }).catch(function(error) {
                console.log(error)
                if(error.response){
                    console.log(error.response.data)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                    alert(error.response.data.message['__all__'])
                }
                else{
                    alert("An error occured.")
                }
                app.status = "Bad request."
            })
        }, 500),
    }
})

var app = new Vue({
    el: '#app',
    data: {
        questions: [],
        text: [],
        status: "",
        paper: "",
    },
    watch: {
        text: function(){
            this.populateRes()
            show.populateQset()
        }
    },
    methods: {
        addToSet: function(){
            alert("I'll add this question to the set on the right via an api call.")
        },
        populateRes: _.debounce(function(){
            var app = this
            app.status = "Searching..."
            axios.get(
                "http://127.0.0.1:8000/question/", {
                    params: {
                        text: app.text,
                        tag: 2,
                    }
                }
            ).then(function (response) {
                console.log(response.data)
                app.questions = response.data
                app.status = "Found " + app.questions.length + " questions."
            }).catch(function(error) {
                console.log(error)
                if(error.response){
                    console.log(error.response.data)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                    alert(error.response.data.message['__all__'])
                }
                else{
                    alert("An error occured.")
                }
                app.status = "Bad request."
            })
        }, 500),
    },
})
