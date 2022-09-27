from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QMessageBox)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys,os
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class VideoPlayer(QMainWindow):
  try:
      a = sys._MEIPASS
  except AttributeError:
      a = os.getcwd()
  path = os.path.join(a)
  limit=10
  def __init__(self):
      super().__init__()
      self.setWindowTitle("ONLY FOR 김금운")
      self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
      videoWidget = QVideoWidget()
      self.playButton = QPushButton()
      #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
      self.playButton.setIcon(QIcon(self.path+'/lock/p.ico'))
      self.playButton.clicked.connect(self.play)

      self.positionSlider = QSlider(Qt.Horizontal)
      self.positionSlider.setRange(0, 0)
      self.positionSlider.sliderMoved.connect(self.setPosition)

      self.error = QLabel()
      self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

      openButton = QPushButton("영상받아오기")
      openButton.setToolTip("Open Video File")
      openButton.setStatusTip("Open Video File")
      openButton.setFixedHeight(24)
      openButton.clicked.connect(self.openFile)

      # self.movie = QMovie("a.gif")
      # self.movie.frameChanged.connect(self.repaint)
      # self.movie.start()
      # self.movie.setScaledSize(QSize(100,100))
      self.msg = QMessageBox()
      self.msg.setWindowTitle("플레이플리즈 영상 안내")

      # Create a widget for window contents
      wid = QWidget(self)
      self.setCentralWidget(wid)

      # Create layouts to place inside widget
      controlLayout = QHBoxLayout()
      controlLayout.setContentsMargins(0, 0, 0, 0)
      controlLayout.addWidget(self.playButton)
      controlLayout.addWidget(self.positionSlider)


      layout = QVBoxLayout()
      layout.addWidget(videoWidget)
      layout.addLayout(controlLayout)
      layout.addWidget(self.error)
      layout.addWidget(openButton)
       # Set widget to contain window contents
      wid.setLayout(layout)

      self.mediaPlayer.setVideoOutput(videoWidget)
      self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
      self.mediaPlayer.positionChanged.connect(self.positionChanged)
      self.mediaPlayer.durationChanged.connect(self.durationChanged)
      self.mediaPlayer.error.connect(self.handleError)
  # def paintEvent(self, event):
  #     currentFrame = self.movie.currentPixmap()
  #     frameRect = currentFrame.rect()
  #     frameRect.moveCenter(self.rect().center())
  #     if frameRect.intersects(event.rect()):
  #         painter = QPainter(self)
  #         painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)


  def exitCall(self):
      sys.exit(app.exec_())

  def openFile(self):
      try:
          wd = sys._MEIPASS
      except AttributeError:
          wd = os.getcwd()
      file_path = os.path.join(wd)
      # self.mediaPlayer.setMedia(
      #         QMediaContent(QUrl("https://playplz.s3.ap-northeast-2.amazonaws.com/gift.mp4")) )
      # current_path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
      current_path=file_path
      path='file:///'+current_path+'/lock/gift_brand.mp4'
      self.mediaPlayer.setMedia(
              QMediaContent(QUrl(path)))
      # self.msg.setText(file_path)
      # self.msg.exec_()
      if self.limit>0:
          self.limit-=1
          self.msg.setText("재생가능 횟수 {0}회 남았습니다".format(self.limit))
          self.msg.exec_()
          self.playButton.setEnabled(True)
      else:
          self.msg.setText("재생가능 횟수를 모두 쓰셨습니다. 아래 주소로 이동해 추가 결제 부탁드립니다")
          self.msg.exec_()
  def play(self):
      if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
          self.mediaPlayer.pause()
      else:
          self.mediaPlayer.play()



  def mediaStateChanged(self, state):
      if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
          self.playButton.setIcon(
                  self.style().standardIcon(QStyle.SP_MediaPause))
      else:
          self.playButton.setIcon(QIcon(self.path+'/lock/p.ico'))

  def positionChanged(self, position):
      self.positionSlider.setValue(position)

  def durationChanged(self, duration):
      self.positionSlider.setRange(0, duration)

  def setPosition(self, position):
      self.mediaPlayer.setPosition(position)

  def handleError(self):
      self.playButton.setEnabled(False)
      self.error.setText("Error: " + self.mediaPlayer.errorString())


  app = QApplication(sys.argv)
  videoplayer = VideoPlayer()
  videoplayer.resize(640, 480)
  videoplayer.show()
  sys.exit(app.exec_())