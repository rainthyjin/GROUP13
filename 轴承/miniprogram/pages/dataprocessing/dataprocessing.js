// pages/dataprocessing/dataprocessing.js
var util = require('../../util/util.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  processing() {
    for (var i = 1; i < 143; i++) {
    util.reqFunc('https://api.phmlearn.com/component/upload/2/212',
      {
        "access_token": app.globalData.access_token,
        "file_name": "TEST"+i+".csv",
      }, function(res){
        app.globalData.output_fileName = app.globalData.output_fileName.concat(res.data.data.file_name);
       
      })
    }
    setTimeout(function () {
      wx.showToast({
        title: '处理成功',
        duration: 2000})
    }, 67000)
    setTimeout(function () {
   
      wx.navigateTo({
        url: '../model/model' ,
      })
    }, 69000)
    
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