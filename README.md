---
title: Defect detection for Printed Circuit Boards
emoji: 🔌
colorFrom: green
colorTo: gray
sdk: gradio
app_file: app.py
pinned: false
---

# Defect detection for Printed Circuit Boards

> AI to detect and recognize six types of defects on printed circuit boards: missing hole, mouse bite, open circuit, short, spur, and spurious copper.

## Table of contents

- [General information](#general-information)
- [Dataset](#dataset)
- [How does it work](#how-does-it-work)

## [Live demo](https://huggingface.co/spaces/itsyoboieltr/pcb)

## General information

This is an AI that was trained on images of defect printed circuit boards to carry out defect detection and recognition. It can recognize six types of defects on printed circuit boards: missing hole, mouse bite, open circuit, short, spur, and spurious copper.

<img width="300" src="https://user-images.githubusercontent.com/72046715/227010274-b40565a4-787e-471f-813f-385a8b80aa51.jpg">

## Dataset

The Open Lab on Human Robot Interaction of Peking University released the PCB defect dataset.

R. Ding, L. Dai, G. Li and H. Liu, "TDD-net: a tiny defect detection network for printed circuit boards," in CAAI Transactions on Intelligence Technology, vol. 4, no. 2, pp. 110-116, 6 2019, doi: 10.1049/trit.2019.0019.

<img width="600" src="https://user-images.githubusercontent.com/72046715/227010391-b3738ad7-a5d5-45cc-a97e-7c7f75b795cf.png">

## How does it work

Technologies used:

- [RT-DETR](https://github.com/lyuwenyu/RT-DETR): Object detection model to detect and recognize defects.
