def launch_relay_signal_deivce_v2(imei, duration, data=None,high=500, low=4294967295):
    dbg((imei, duration))
    imei = imei
    duration = duration
    pulse = 1
    money = pulse
    device_type = 0
    high = 500
    low = 4294967295   # 'ffffffff'

    mongodata = {
        'imei': imei,
        'datagram_type': 1,
        'device_type': device_type,
        'duration': duration,
        'high': high,
        'low': low,
        'pulse': pulse
    }
    if data == None:
        data = bytearray([0x54, device_type])
        data += money.to_bytes(4, 'big')
        data += duration.to_bytes(4, 'big')
        data += high.to_bytes(4, 'big')
        data += low.to_bytes(4, 'big')
        data += pulse.to_bytes(4, 'big')

    dbg(data)
    try:
        result = tool.send_data_to_device(
            'deveventreq', imei, data, need_to_wait=True)
        if result and result['result']:
            mongodata['result'] = 0     # 成功
            dbapi.insert_datagram(mongodata)

            # added 
            # 发送语音内容
            device = dbapi.get_device(imei=imei)
            voice = dbapi.get_voice(agent_id=device.owner_agent_id, using=1)
            if voice:

                tool.send_data_to_device(
                    'ttsrelay', imei, voice.start_voice.encode('gb2312'), need_to_wait=False)
                tool.send_data_to_device(
                    'ttsend', imei, voice.end_voice.encode('gb2312'), need_to_wait=False)

            return True, json.dumps({'code': 0, 'msg': ''})
        else:
            mongodata['result'] = 1     # 设备正在运行
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8002, 'msg': '设备正在运行'})
    except error.ApiError as e:
        if e.error_no == 8001:
            mongodata['result'] = 2     # 设备连接超时
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8001, 'msg': '设备连接超时'})
        else:
            mongodata['result'] = 3     # server error
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 99, 'msg': 'server error'})
    except:
        mongodata['result'] = 3     # server error
        dbapi.insert_datagram(mongodata)
        return False, json.dumps({'code': 99, 'msg': 'server error'})


def launch_pulse_signal_deivce(imei, pulse, high=50, low=50):
    dbg((imei, pulse, high, low))
    imei = imei
    pulse = pulse
    money = pulse
    device_type = 1
    duration = 5
    high = high
    low  = low

    mongodata = {
        'imei': imei,
        'datagram_type': 1,
        'device_type': device_type,
        'duration': duration,
        'high': high,
        'low': low,
        'pulse': pulse
    }

    data = bytearray([0x54, device_type])

    data += money.to_bytes(4, 'big')
    data += duration.to_bytes(4, 'big')
    data += high.to_bytes(4, 'big')
    data += low.to_bytes(4, 'big')
    data += pulse.to_bytes(4, 'big')

    dbg(data)
    try:
        result = tool.send_data_to_device(
            'deveventreq', imei, data, need_to_wait=True)
        if result and result['result']:
            mongodata['result'] = 0     # 成功
            dbapi.insert_datagram(mongodata)
            # added 
            # 发送语音内容
            device = dbapi.get_device(imei=imei)
            voice = dbapi.get_voice(agent_id=device.owner_agent_id, using=1)
            if voice:
                tool.send_data_to_device(
                    'ttspulse', imei, voice.pulse_voice.encode('gb2312'), need_to_wait=False)

            return True, json.dumps({'code': 0, 'msg': ''})
        else:
            mongodata['result'] = 1     # 设备正在运行
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8002, 'msg': '设备正在运行'})
    except error.ApiError as e:
        if e.error_no == 8001:
            mongodata['result'] = 2     # 设备连接超时
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8001, 'msg': '设备连接超时'})
        else:
            mongodata['result'] = 3     # server error
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 99, 'msg': 'server error'})
    except:
        mongodata['result'] = 3     # server error
        dbapi.insert_datagram(mongodata)
        return False, json.dumps({'code': 99, 'msg': 'server error'})


def launch_com_port_deivce(imei, value, com_time, high=50, low=50):
    dbg((imei, value, com_time, high, low))
    imei = imei
    pulse = value
    money = value
    device_type = 1
    duration = com_time
    high = high
    low  = low

    mongodata = {
        'imei': imei,
        'datagram_type': 1,
        'device_type': device_type,
        'duration': duration,
        'high': high,
        'low': low,
        'pulse': pulse
    }
    data = bytearray([0x54, device_type])

    data += money.to_bytes(4, 'big')
    data += duration.to_bytes(4, 'big')
    data += high.to_bytes(4, 'big')
    data += low.to_bytes(4, 'big')
    data += pulse.to_bytes(4, 'big')

    dbg(data)
    try:
        result = tool.send_data_to_device(
            'deveventreq', imei, data, need_to_wait=True)
        if result and result['result']:
            # added
            # 发送语音内容
            device = dbapi.get_device(imei=imei)
            voice = dbapi.get_voice(agent_id=device.owner_agent_id, using=1)
            if voice:
                dbg('voice:%s' % voice.start_voice)
                tool.send_data_to_device(
                    'ttsrelay', imei, voice.start_voice.encode('gb2312'), need_to_wait=False)
                tool.send_data_to_device(
                    'ttsend', imei, voice.end_voice.encode('gb2312'), need_to_wait=False)

            return True, json.dumps({'code': 0, 'msg': ''})
        else:
            return False, json.dumps({'code': 8002, 'msg': '设备正在运行'})
    except error.ApiError as e:
        if e.error_no == 8001:
            mongodata['result'] = 2     # 设备连接超时
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8001, 'msg': '设备连接超时'})
        else:
            mongodata['result'] = 3     # server error
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 99, 'msg': 'server error'})
    except:
        mongodata['result'] = 3     # server error
        dbapi.insert_datagram(mongodata)
        return False, json.dumps({'code': 99, 'msg': 'server error'})

