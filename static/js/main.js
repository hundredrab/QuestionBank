var show = new Vue({
  el: '#show',
  data: {
    qset: {
      id: '',
      questions:'',
      total_marks:''
    },
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
    whitelist: "",
    blacklist: "",
  },
  watch: {
    text: function(){
      this.populateRes()
      //show.populateQset()
    },
    whitelist: function(){
      this.populateRes()
      //show.populateQset()
    },
    blacklist: function(){
      this.populateRes()
      //show.populateQset()
    }
  },
  methods: {
    addToSet: function(qid){
      var app = this
      axios.get(
        "http://127.0.0.1:8000/question/add_to_qset/"+(id), {
          params: {
            qpk: qid,
          }
        }
      ).then(function (response) {
        console.log(response.data)
        show.populateQset()
      }).catch(function(error) {
        console.log(error)
        if(error.response){
          console.log(error.response)
          //console.log(error.response.status)
          //console.log(error.response.headers)
          //alert(error.response.data.message['__all__'])
        }
        else{
          alert("An error occured.")
        }
      })
    },
    populateRes: _.debounce(function(){
      var app = this
      app.status = "Searching..."
      axios.get(
        "http://127.0.0.1:8000/question/", {
          params: {
            text: app.text,
            whitelist: app.whitelist,
            blacklist: app.blacklist,
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
