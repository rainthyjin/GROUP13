// pages/model/model.js
var util = require('../../util/util.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },


  model() {
    for(var i=0;i<142;i++){
    util.reqFunc('https://api.phmlearn.com/component/upload/ML/model/132/211',
      {
        "access_token": app.globalData.access_token,
        "file_name": app.globalData.output_fileName[i],
      },function(res){
        app.globalData.predict = app.globalData.predict.concat(res.data.data.predict);
    
        app.globalData.predict1=app.globalData.predict.slice(0,10);
        app.globalData.predict2=app.globalData.predict.slice(10,20);
        app.globalData.predict3=app.globalData.predict.slice(20,30);
        app.globalData.predict4=app.globalData.predict.slice(30,40);
        app.globalData.predict5=app.globalData.predict.slice(40,50);
        app.globalData.predict6=app.globalData.predict.slice(50,60);
        app.globalData.predict7=app.globalData.predict.slice(60,70);
        app.globalData.predict8=app.globalData.predict.slice(70,80);
        app.globalData.predict9=app.globalData.predict.slice(80,90);
        app.globalData.predict10=app.globalData.predict.slice(90,100);
        app.globalData.predict11=app.globalData.predict.slice(100,110);
        app.globalData.predict12=app.globalData.predict.slice(110,120);
        app.globalData.predict13=app.globalData.predict.slice(120,130);
        app.globalData.predict14=app.globalData.predict.slice(130,142);
        let counts = (arr, value) => arr.reduce((a, v) => v === value ? a + 1 : a + 0, 0);
        app.globalData.normal[0]=counts(app.globalData.predict1,0);
        app.globalData.error[0]=10-counts(app.globalData.predict1,0);
        app.globalData.normal[1]=counts(app.globalData.predict2,0);
        app.globalData.error[1]=10-counts(app.globalData.predict2,0);
        app.globalData.normal[2]=counts(app.globalData.predict3,0);
        app.globalData.error[2]=10-counts(app.globalData.predict3,0);
        app.globalData.normal[3]=counts(app.globalData.predict4,0);
        app.globalData.error[3]=10-counts(app.globalData.predict4,0);
        app.globalData.normal[4]=counts(app.globalData.predict5,0);
        app.globalData.error[4]=10-counts(app.globalData.predict5,0);
        app.globalData.normal[5]=counts(app.globalData.predict6,0);
        app.globalData.error[5]=10-counts(app.globalData.predict6,0);
        app.globalData.normal[6]=counts(app.globalData.predict7,0);
        app.globalData.error[6]=10-counts(app.globalData.predict7,0);
        app.globalData.normal[7]=counts(app.globalData.predict8,0);
        app.globalData.error[7]=10-counts(app.globalData.predict8,0);
        app.globalData.normal[8]=counts(app.globalData.predict9,0);
        app.globalData.error[8]=10-counts(app.globalData.predict9,0);
        app.globalData.normal[9]=counts(app.globalData.predict10,0);
        app.globalData.error[9]=10-counts(app.globalData.predict10,0);
        app.globalData.normal[10]=counts(app.globalData.predict11,0);
        app.globalData.error[10]=10-counts(app.globalData.predict11,0);
        app.globalData.normal[11]=counts(app.globalData.predict12,0);
        app.globalData.error[11]=10-counts(app.globalData.predict12,0);
        app.globalData.normal[12]=counts(app.globalData.predict13,0);
        app.globalData.error[12]=10-counts(app.globalData.predict13,0);
        app.globalData.normal[13]=counts(app.globalData.predict14,0);
        app.globalData.error[13]=12-counts(app.globalData.predict14,0);

      })
    }
    setTimeout(function () {
      wx.showToast({
        title: '处理成功',
        duration: 2000})
    }, 67000)
    setTimeout(function () {
   
      wx.navigateTo({
        url: '../result/result' ,
      })
    }, 69000)
      app.globalData.time=util.formatTime(new Date());
      console.log(app.globalData.time)
    
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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