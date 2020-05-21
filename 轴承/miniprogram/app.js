//app.js
App({
  onLaunch: function () {
    
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        traceUser: true,
      })
    }

    this.globalData = {
      access_token: "74fbc10c8f92497a9c4a76908ba9c4cc.139ccc39eebf35107f186ffe3510beda",
      output_fileName:[],
      resultArray: [],
      predict:[],
      predict1:[],
      predict2:[],
      predict3:[],
      predict4:[],
      predict5:[],
      predict6:[],
      predict7:[],
      predict8:[],
      predict9:[],
      predict10:[],
      predict11:[],
      predict12:[],
      predict13:[],
      predict14:[],
      time:'',
      normal:[],
      error:[],
     
    }
  }
})
