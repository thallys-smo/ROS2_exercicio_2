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

# Criando o nome do Nó Leitor (Subscriber) e o tópico de publicação ROS image messagesp
subscriberName, topicName = 'camera_subscriber','video_topic' 

def callbackFunction(message):
    # Cria um objeto de conexão
    bridgeObject = CvBridge()
    # Printa uma mensagem de log
    rospy.loginfo("Recebendo vídeo mensagem/frame")
    # Converte de OpenCV para mensagem de imagem ROS
    convertedFrameBackToCV = bridgeObject.imgmsg_to_cv2(message)
    # Mostra a imagem
    cv2.imshow("Camera", convertedFrameBackToCV)
    # Espera 1 milissegundo
    cv2.waitKey(1)

# Iniciando o nó leitor (subscriber)
rospy.init_node(subscriberName, anonymous = True)
# Especificando o topico e typo de mensagem que será recebida
rospy.Subscriber(topicName, Image, callbackFunction)
# configura para o video ficar rodando (spin), até que ctrl + c seja precionado
rospy.spin()
# Fecha a tela do video
cv2.destroyAllWindows()