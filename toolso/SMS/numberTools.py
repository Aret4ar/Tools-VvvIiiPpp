a
    g�`�  �                   @   s,   d dl mZmZ dd� Zdd� Zdd� ZdS )	�    )�geocoder�parsec                 C   s   | d dkr| dd � } | S )Nr   �+�   � )�phoner   r   �8/storage/emulated/0/Script Vip/toolso/SMS/numberTools.py�	normalize   s    r	   c                 C   sX   |dkrTd| d  d | dd�  d | dd�  d	 | dd
�  d	 | d
d�  S d S )N�   r   r   z (r   �   z) �   � �	   �   r   )r   �ir   r   r   �transformPhone   s    r   c                 C   s   t d|  d �}tt�|d��S )Nr   Zen)r   �reprr   Zdescription_for_number)r   Zqueryr   r   r   �
getCountry   s    r   N)Zphonenumbersr   r   r	   r   r   r   r   r   r   �<module>   s   