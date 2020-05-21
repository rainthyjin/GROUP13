// pages/datapreview/datapreview.js
var util = require('../../util/util.js')
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    value1:'',//机组号
    value2:'',//设备状态
    show:false,
    columns1:['100','108','121','133','147','160','172','188','200','212','225','237','249','261'],
    show1:false,
    timer: '',
    timer2: '',
    result: [],
    time:'',
    predict:[]
  },
  
  showPopup: function() {
    this.setData({show:true});
    this.setData({show1:true});
    },

    onClose:function() {
      this.setData({ show: false });
      this.setData({ show1: false });
    },

    getDatas: function (id, arr,callback) {
      var that = this
      wx.request({
        url: 'https://api.phmlearn.com/component/data/zhoucheng ',
        method: 'POST',
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          access_token: app.globalData.access_token,
          divice_id: id,
          atrribute: arr
        },
        success: function (res) {
          callback(res);
          //console.log(res.data);
        
        }
      })
    },

    setDatas: function (Id) {
      this.getDatas(Id, 'DE_time', res => {
        this.setData({
          'result[0]': {
            key: '驱动端振动',
            max: Math.max(...res.data.data.data).toFixed(5),
            min: Math.min(...res.data.data.data).toFixed(5),
            arr: this.setArrData(res.data.data.data),
           
          },
         
          
        })
        
      })
      this.getDatas(Id, 'FE_time', res => {
        this.setData({
          'result[1]': {
            key: '风扇端振动',
            max: Math.max(...res.data.data.data).toFixed(5),
            min: Math.min(...res.data.data.data).toFixed(5),
            arr: this.setArrData(res.data.data.data)
          }
        })
      })
      this.getDatas(Id, 'BA_time', res => {
        this.setData({
          'result[2]': {
            key: '基本加速度',
            max: Math.max(...res.data.data.data).toFixed(5),
            min: Math.min(...res.data.data.data).toFixed(5),
            arr: this.setArrData(res.data.data.data)
          }
        })
      })
      this.getDatas(Id, 'RPM', res => {
        this.setData({
          'result[3]': {
            key: '工作转速',
            max: Math.max(...res.data.data.data).toFixed(5),
            min: Math.min(...res.data.data.data).toFixed(5),
            arr: this.setArrData(res.data.data.data)
          }
        })
        this.startTimer()
        this.setDate()
      })
    },


    onConfirm1(event) {
      const { picker, value, index } = event.detail; 
      this.setData({ value1: value });
      this.setDatas(value);
      this.closeTimer(this.data.timer)
      this.closeTimer(this.data.timer2)
      this.setData({ show: false });
      this.setData({ show1: false });
     // this.setlable(this.data.value1)
      //console.log(this.data.value2)
    },
  
    setArrData: function (arr) {
      for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].toFixed(5)
      }
      return arr
    },

    setDate: function () {
      this.setData({
        timer2: setInterval(() => {
          this.setData({
            time: util.formatTime(new Date())
          })
        }, 1000)
      })
    },
    startTimer: function () {
      this.setData({
        i: 0
      })
      this.setData({
        timer: setInterval(() => {
          if (this.data.i <= 3000) {
            this.setData({
              i: this.data.i + 1
            })
          }
          else {
            this.setData({
              i: 0
            })
            this.closeTimer(this.data.timer)
            this.closeTimer(this.data.timer2)
          }
        }, 1000)
      })
    },
    closeTimer: function (time) {
      clearInterval(time)
    },


    onCancel:function() {
     // Toast('取消');
      this.setData({ show: false });
      this.setData({ show1: false });
    },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      time: app.globalData.time,
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    clearInterval(this.data.timer2)
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})