#!/usr/bin/env python3
# A linha acima indica ao ROS onde está o compilador python

# Permiti que utilizemos ROS com Python
import rospy

# Enviaremos mensagens na forma de imagens, logo importamos Image
from sensor_msgs.msg import Image

# CvBridge é uma biblioteca responsável por converter imagens OpenCV (type cv::Mat)
# Como o nome já indica, é uma ponte (bridge) entre o ROS e a OpenCV
from cv_bridge import CvBridge

# Importar a Opencv
import cv2
#from cv2 import VideoCapture
#from cv2 import waitKey

publisherName, topicName = 'camera_publisher','video_topic'

rospy.init_node(publisherName, anonymous = True)
publisher = rospy.Publisher(topicName, Image, queue_size = 60)

# Transmite as imagens em 30 Hz, , ou seja, 30 imagens por segundo.
rate = rospy.Rate(30)

# Cria a captura de video
videoCaptureObject = cv2.VideoCapture(0)

# Objeto CvBrige para ser utilizado na conversão de Imagens OpenCV para mensagens de imagem ROS
bridgeObject = CvBridge()

# O loop infinito abaixo captura a imagem, a converte e transmite para o topico
while not rospy.is_shutdown():
    # Retorna dois valores, sendo o primeiro um boleano que indica sucesso ou falha
    # O segundo é o frame em si
    returnValue, capturedFrame = videoCaptureObject.read()
    if returnValue == True:
        # Printa uma mensagem de log
        rospy.loginfo('Video frame captured and publisher')
        # Converte de OpenCV para mensagem de imagem ROS
        imageToTransmit = bridgeObject.cv2_to_imgmsg(capturedFrame)
        # Publica a imagem convertida pelo topico
        publisher.publish(imageToTransmit)
    # Espera um certo tempo para que a taxa de transmissão seja atingida
    rate.sleep()


