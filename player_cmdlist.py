cmdlist_dict = {'af_add': {'command': 'af_add',
            'comment': 'MPlayer command: af_add String',
            'pycommand': 'af_add(<str>)',
            'types': ['str']},
 'af_clr': {'command': 'af_clr',
            'comment': 'MPlayer command: af_clr',
            'pycommand': 'af_clr()',
            'types': []},
 'af_cmdline': {'command': 'af_cmdline',
                'comment': 'MPlayer command: af_cmdline String String',
                'pycommand': 'af_cmdline(<str>, <str>)',
                'types': ['str', 'str']},
 'af_del': {'command': 'af_del',
            'comment': 'MPlayer command: af_del String',
            'pycommand': 'af_del(<str>)',
            'types': ['str']},
 'af_switch': {'command': 'af_switch',
               'comment': 'MPlayer command: af_switch String',
               'pycommand': 'af_switch(<str>)',
               'types': ['str']},
 'alt_src_step': {'command': 'alt_src_step',
                  'comment': 'MPlayer command: alt_src_step Integer',
                  'pycommand': 'alt_src_step(<int>)',
                  'types': ['int']},
 'ass_use_margins': {'command': 'ass_use_margins',
                     'comment': 'MPlayer command: ass_use_margins [Integer]',
                     'pycommand': 'ass_use_margins([, <int>])',
                     'types': ['int']},
 'audio_delay': {'command': 'audio_delay',
                 'comment': 'MPlayer command: audio_delay Float [Integer]',
                 'pycommand': 'audio_delay(<float>[, <int>])',
                 'types': ['float', 'int']},
 'balance': {'command': 'balance',
             'comment': 'MPlayer command: balance Float [Integer]',
             'pycommand': 'balance(<float>[, <int>])',
             'types': ['float', 'int']},
 'brightness': {'command': 'brightness',
                'comment': 'MPlayer command: brightness Integer [Integer]',
                'pycommand': 'brightness(<int>[, <int>])',
                'types': ['int', 'int']},
 'capturing': {'command': 'capturing',
               'comment': 'MPlayer command: capturing',
               'pycommand': 'capturing()',
               'types': []},
 'change_rectangle': {'command': 'change_rectangle',
                      'comment': 'MPlayer command: change_rectangle Integer Integer',
                      'pycommand': 'change_rectangle(<int>, <int>)',
                      'types': ['int', 'int']},
 'contrast': {'command': 'contrast',
              'comment': 'MPlayer command: contrast Integer [Integer]',
              'pycommand': 'contrast(<int>[, <int>])',
              'types': ['int', 'int']},
 'dvb_set_channel': {'command': 'dvb_set_channel',
                     'comment': 'MPlayer command: dvb_set_channel Integer Integer',
                     'pycommand': 'dvb_set_channel(<int>, <int>)',
                     'types': ['int', 'int']},
 'dvdnav': {'command': 'dvdnav',
            'comment': 'MPlayer command: dvdnav String',
            'pycommand': 'dvdnav(<str>)',
            'types': ['str']},
 'edl_mark': {'command': 'edl_mark',
              'comment': 'MPlayer command: edl_mark',
              'pycommand': 'edl_mark()',
              'types': []},
 'forced_subs_only': {'command': 'forced_subs_only',
                      'comment': 'MPlayer command: forced_subs_only [Integer]',
                      'pycommand': 'forced_subs_only([, <int>])',
                      'types': ['int']},
 'frame_drop': {'command': 'frame_drop',
                'comment': 'MPlayer command: frame_drop [Integer]',
                'pycommand': 'frame_drop([, <int>])',
                'types': ['int']},
 'frame_step': {'command': 'frame_step',
                'comment': 'MPlayer command: frame_step',
                'pycommand': 'frame_step()',
                'types': []},
 'gamma': {'command': 'gamma',
           'comment': 'MPlayer command: gamma Integer [Integer]',
           'pycommand': 'gamma(<int>[, <int>])',
           'types': ['int', 'int']},
 'get_audio_bitrate': {'command': 'get_audio_bitrate',
                       'comment': 'MPlayer command: get_audio_bitrate',
                       'pycommand': 'get_audio_bitrate()',
                       'types': []},
 'get_audio_codec': {'command': 'get_audio_codec',
                     'comment': 'MPlayer command: get_audio_codec',
                     'pycommand': 'get_audio_codec()',
                     'types': []},
 'get_audio_samples': {'command': 'get_audio_samples',
                       'comment': 'MPlayer command: get_audio_samples',
                       'pycommand': 'get_audio_samples()',
                       'types': []},
 'get_file_name': {'command': 'get_file_name',
                   'comment': 'MPlayer command: get_file_name',
                   'pycommand': 'get_file_name()',
                   'types': []},
 'get_meta_album': {'command': 'get_meta_album',
                    'comment': 'MPlayer command: get_meta_album',
                    'pycommand': 'get_meta_album()',
                    'types': []},
 'get_meta_artist': {'command': 'get_meta_artist',
                     'comment': 'MPlayer command: get_meta_artist',
                     'pycommand': 'get_meta_artist()',
                     'types': []},
 'get_meta_comment': {'command': 'get_meta_comment',
                      'comment': 'MPlayer command: get_meta_comment',
                      'pycommand': 'get_meta_comment()',
                      'types': []},
 'get_meta_genre': {'command': 'get_meta_genre',
                    'comment': 'MPlayer command: get_meta_genre',
                    'pycommand': 'get_meta_genre()',
                    'types': []},
 'get_meta_title': {'command': 'get_meta_title',
                    'comment': 'MPlayer command: get_meta_title',
                    'pycommand': 'get_meta_title()',
                    'types': []},
 'get_meta_track': {'command': 'get_meta_track',
                    'comment': 'MPlayer command: get_meta_track',
                    'pycommand': 'get_meta_track()',
                    'types': []},
 'get_meta_year': {'command': 'get_meta_year',
                   'comment': 'MPlayer command: get_meta_year',
                   'pycommand': 'get_meta_year()',
                   'types': []},
 'get_percent_pos': {'command': 'get_percent_pos',
                     'comment': 'MPlayer command: get_percent_pos',
                     'pycommand': 'get_percent_pos()',
                     'types': []},
 'get_property': {'command': 'get_property',
                  'comment': 'MPlayer command: get_property String',
                  'pycommand': 'get_property(<str>)',
                  'types': ['str']},
 'get_sub_visibility': {'command': 'get_sub_visibility',
                        'comment': 'MPlayer command: get_sub_visibility',
                        'pycommand': 'get_sub_visibility()',
                        'types': []},
 'get_time_length': {'command': 'get_time_length',
                     'comment': 'MPlayer command: get_time_length',
                     'pycommand': 'get_time_length()',
                     'types': []},
 'get_time_pos': {'command': 'get_time_pos',
                  'comment': 'MPlayer command: get_time_pos',
                  'pycommand': 'get_time_pos()',
                  'types': []},
 'get_video_bitrate': {'command': 'get_video_bitrate',
                       'comment': 'MPlayer command: get_video_bitrate',
                       'pycommand': 'get_video_bitrate()',
                       'types': []},
 'get_video_codec': {'command': 'get_video_codec',
                     'comment': 'MPlayer command: get_video_codec',
                     'pycommand': 'get_video_codec()',
                     'types': []},
 'get_video_resolution': {'command': 'get_video_resolution',
                          'comment': 'MPlayer command: get_video_resolution',
                          'pycommand': 'get_video_resolution()',
                          'types': []},
 'get_vo_fullscreen': {'command': 'get_vo_fullscreen',
                       'comment': 'MPlayer command: get_vo_fullscreen',
                       'pycommand': 'get_vo_fullscreen()',
                       'types': []},
 'hue': {'command': 'hue',
         'comment': 'MPlayer command: hue Integer [Integer]',
         'pycommand': 'hue(<int>[, <int>])',
         'types': ['int', 'int']},
 'key_down_event': {'command': 'key_down_event',
                    'comment': 'MPlayer command: key_down_event Integer',
                    'pycommand': 'key_down_event(<int>)',
                    'types': ['int']},
 'loadfile': {'command': 'loadfile',
              'comment': 'MPlayer command: loadfile String [Integer]',
              'pycommand': 'loadfile(<str>[, <int>])',
              'types': ['str', 'int']},
 'loadlist': {'command': 'loadlist',
              'comment': 'MPlayer command: loadlist String [Integer]',
              'pycommand': 'loadlist(<str>[, <int>])',
              'types': ['str', 'int']},
 'loop': {'command': 'loop',
          'comment': 'MPlayer command: loop Integer [Integer]',
          'pycommand': 'loop(<int>[, <int>])',
          'types': ['int', 'int']},
 'mute': {'command': 'mute',
          'comment': 'MPlayer command: mute [Integer]',
          'pycommand': 'mute([, <int>])',
          'types': ['int']},
 'osd': {'command': 'osd',
         'comment': 'MPlayer command: osd [Integer]',
         'pycommand': 'osd([, <int>])',
         'types': ['int']},
 'osd_show_progression': {'command': 'osd_show_progression',
                          'comment': 'MPlayer command: osd_show_progression',
                          'pycommand': 'osd_show_progression()',
                          'types': []},
 'osd_show_property_te': {'command': 'osd_show_property_te',
                          'comment': 'MPlayer command: osd_show_property_te String [Integer] [Integer]',
                          'pycommand': 'osd_show_property_te(<str>[, <int>][, <int>])',
                          'types': ['str', 'int', 'int']},
 'osd_show_text': {'command': 'osd_show_text',
                   'comment': 'MPlayer command: osd_show_text String [Integer] [Integer]',
                   'pycommand': 'osd_show_text(<str>[, <int>][, <int>])',
                   'types': ['str', 'int', 'int']},
 'panscan': {'command': 'panscan',
             'comment': 'MPlayer command: panscan Float [Integer]',
             'pycommand': 'panscan(<float>[, <int>])',
             'types': ['float', 'int']},
 'pause': {'command': 'pause',
           'comment': 'MPlayer command: pause',
           'pycommand': 'pause()',
           'types': []},
 'pt_step': {'command': 'pt_step',
             'comment': 'MPlayer command: pt_step Integer [Integer]',
             'pycommand': 'pt_step(<int>[, <int>])',
             'types': ['int', 'int']},
 'pt_up_step': {'command': 'pt_up_step',
                'comment': 'MPlayer command: pt_up_step Integer [Integer]',
                'pycommand': 'pt_up_step(<int>[, <int>])',
                'types': ['int', 'int']},
 'quit': {'command': 'quit',
          'comment': 'MPlayer command: quit [Integer]',
          'pycommand': 'quit([, <int>])',
          'types': ['int']},
 'run': {'command': 'run',
         'comment': 'MPlayer command: run String',
         'pycommand': 'run(<str>)',
         'types': ['str']},
 'saturation': {'command': 'saturation',
                'comment': 'MPlayer command: saturation Integer [Integer]',
                'pycommand': 'saturation(<int>[, <int>])',
                'types': ['int', 'int']},
 'screenshot': {'command': 'screenshot',
                'comment': 'MPlayer command: screenshot [Integer] [Integer]',
                'pycommand': 'screenshot([, <int>][, <int>])',
                'types': ['int', 'int']},
 'seek': {'command': 'seek',
          'comment': 'MPlayer command: seek Float [Integer] [Integer]',
          'pycommand': 'seek(<float>[, <int>][, <int>])',
          'types': ['float', 'int', 'int']},
 'seek_chapter': {'command': 'seek_chapter',
                  'comment': 'MPlayer command: seek_chapter Integer [Integer]',
                  'pycommand': 'seek_chapter(<int>[, <int>])',
                  'types': ['int', 'int']},
 'set_mouse_pos': {'command': 'set_mouse_pos',
                   'comment': 'MPlayer command: set_mouse_pos Integer Integer',
                   'pycommand': 'set_mouse_pos(<int>, <int>)',
                   'types': ['int', 'int']},
 'set_property': {'command': 'set_property',
                  'comment': 'MPlayer command: set_property String String',
                  'pycommand': 'set_property(<str>, <str>)',
                  'types': ['str', 'str']},
 'set_property_osd': {'command': 'set_property_osd',
                      'comment': 'MPlayer command: set_property_osd String String',
                      'pycommand': 'set_property_osd(<str>, <str>)',
                      'types': ['str', 'str']},
 'speed_incr': {'command': 'speed_incr',
                'comment': 'MPlayer command: speed_incr Float',
                'pycommand': 'speed_incr(<float>)',
                'types': ['float']},
 'speed_mult': {'command': 'speed_mult',
                'comment': 'MPlayer command: speed_mult Float',
                'pycommand': 'speed_mult(<float>)',
                'types': ['float']},
 'speed_set': {'command': 'speed_set',
               'comment': 'MPlayer command: speed_set Float',
               'pycommand': 'speed_set(<float>)',
               'types': ['float']},
 'step_property': {'command': 'step_property',
                   'comment': 'MPlayer command: step_property String [Float] [Integer]',
                   'pycommand': 'step_property(<str>[, <float>][, <int>])',
                   'types': ['str', 'float', 'int']},
 'step_property_osd': {'command': 'step_property_osd',
                       'comment': 'MPlayer command: step_property_osd String [Float] [Integer]',
                       'pycommand': 'step_property_osd(<str>[, <float>][, <int>])',
                       'types': ['str', 'float', 'int']},
 'stop': {'command': 'stop',
          'comment': 'MPlayer command: stop',
          'pycommand': 'stop()',
          'types': []},
 'sub_alignment': {'command': 'sub_alignment',
                   'comment': 'MPlayer command: sub_alignment [Integer]',
                   'pycommand': 'sub_alignment([, <int>])',
                   'types': ['int']},
 'sub_delay': {'command': 'sub_delay',
               'comment': 'MPlayer command: sub_delay Float [Integer]',
               'pycommand': 'sub_delay(<float>[, <int>])',
               'types': ['float', 'int']},
 'sub_demux': {'command': 'sub_demux',
               'comment': 'MPlayer command: sub_demux [Integer]',
               'pycommand': 'sub_demux([, <int>])',
               'types': ['int']},
 'sub_file': {'command': 'sub_file',
              'comment': 'MPlayer command: sub_file [Integer]',
              'pycommand': 'sub_file([, <int>])',
              'types': ['int']},
 'sub_load': {'command': 'sub_load',
              'comment': 'MPlayer command: sub_load String',
              'pycommand': 'sub_load(<str>)',
              'types': ['str']},
 'sub_log': {'command': 'sub_log',
             'comment': 'MPlayer command: sub_log',
             'pycommand': 'sub_log()',
             'types': []},
 'sub_pos': {'command': 'sub_pos',
             'comment': 'MPlayer command: sub_pos Integer [Integer]',
             'pycommand': 'sub_pos(<int>[, <int>])',
             'types': ['int', 'int']},
 'sub_remove': {'command': 'sub_remove',
                'comment': 'MPlayer command: sub_remove [Integer]',
                'pycommand': 'sub_remove([, <int>])',
                'types': ['int']},
 'sub_scale': {'command': 'sub_scale',
               'comment': 'MPlayer command: sub_scale Float [Integer]',
               'pycommand': 'sub_scale(<float>[, <int>])',
               'types': ['float', 'int']},
 'sub_select': {'command': 'sub_select',
                'comment': 'MPlayer command: sub_select [Integer]',
                'pycommand': 'sub_select([, <int>])',
                'types': ['int']},
 'sub_source': {'command': 'sub_source',
                'comment': 'MPlayer command: sub_source [Integer]',
                'pycommand': 'sub_source([, <int>])',
                'types': ['int']},
 'sub_step': {'command': 'sub_step',
              'comment': 'MPlayer command: sub_step Integer [Integer]',
              'pycommand': 'sub_step(<int>[, <int>])',
              'types': ['int', 'int']},
 'sub_visibility': {'command': 'sub_visibility',
                    'comment': 'MPlayer command: sub_visibility [Integer]',
                    'pycommand': 'sub_visibility([, <int>])',
                    'types': ['int']},
 'sub_vob': {'command': 'sub_vob',
             'comment': 'MPlayer command: sub_vob [Integer]',
             'pycommand': 'sub_vob([, <int>])',
             'types': ['int']},
 'switch_angle': {'command': 'switch_angle',
                  'comment': 'MPlayer command: switch_angle [Integer]',
                  'pycommand': 'switch_angle([, <int>])',
                  'types': ['int']},
 'switch_audio': {'command': 'switch_audio',
                  'comment': 'MPlayer command: switch_audio [Integer]',
                  'pycommand': 'switch_audio([, <int>])',
                  'types': ['int']},
 'switch_ratio': {'command': 'switch_ratio',
                  'comment': 'MPlayer command: switch_ratio [Float]',
                  'pycommand': 'switch_ratio([, <float>])',
                  'types': ['float']},
 'switch_title': {'command': 'switch_title',
                  'comment': 'MPlayer command: switch_title [Integer]',
                  'pycommand': 'switch_title([, <int>])',
                  'types': ['int']},
 'switch_vsync': {'command': 'switch_vsync',
                  'comment': 'MPlayer command: switch_vsync [Integer]',
                  'pycommand': 'switch_vsync([, <int>])',
                  'types': ['int']},
 'teletext_add_dec': {'command': 'teletext_add_dec',
                      'comment': 'MPlayer command: teletext_add_dec String',
                      'pycommand': 'teletext_add_dec(<str>)',
                      'types': ['str']},
 'teletext_go_link': {'command': 'teletext_go_link',
                      'comment': 'MPlayer command: teletext_go_link Integer',
                      'pycommand': 'teletext_go_link(<int>)',
                      'types': ['int']},
 'tv_last_channel': {'command': 'tv_last_channel',
                     'comment': 'MPlayer command: tv_last_channel',
                     'pycommand': 'tv_last_channel()',
                     'types': []},
 'tv_set_brightness': {'command': 'tv_set_brightness',
                       'comment': 'MPlayer command: tv_set_brightness Integer [Integer]',
                       'pycommand': 'tv_set_brightness(<int>[, <int>])',
                       'types': ['int', 'int']},
 'tv_set_channel': {'command': 'tv_set_channel',
                    'comment': 'MPlayer command: tv_set_channel String',
                    'pycommand': 'tv_set_channel(<str>)',
                    'types': ['str']},
 'tv_set_contrast': {'command': 'tv_set_contrast',
                     'comment': 'MPlayer command: tv_set_contrast Integer [Integer]',
                     'pycommand': 'tv_set_contrast(<int>[, <int>])',
                     'types': ['int', 'int']},
 'tv_set_freq': {'command': 'tv_set_freq',
                 'comment': 'MPlayer command: tv_set_freq Float',
                 'pycommand': 'tv_set_freq(<float>)',
                 'types': ['float']},
 'tv_set_hue': {'command': 'tv_set_hue',
                'comment': 'MPlayer command: tv_set_hue Integer [Integer]',
                'pycommand': 'tv_set_hue(<int>[, <int>])',
                'types': ['int', 'int']},
 'tv_set_norm': {'command': 'tv_set_norm',
                 'comment': 'MPlayer command: tv_set_norm String',
                 'pycommand': 'tv_set_norm(<str>)',
                 'types': ['str']},
 'tv_set_saturation': {'command': 'tv_set_saturation',
                       'comment': 'MPlayer command: tv_set_saturation Integer [Integer]',
                       'pycommand': 'tv_set_saturation(<int>[, <int>])',
                       'types': ['int', 'int']},
 'tv_start_scan': {'command': 'tv_start_scan',
                   'comment': 'MPlayer command: tv_start_scan',
                   'pycommand': 'tv_start_scan()',
                   'types': []},
 'tv_step_chanlist': {'command': 'tv_step_chanlist',
                      'comment': 'MPlayer command: tv_step_chanlist',
                      'pycommand': 'tv_step_chanlist()',
                      'types': []},
 'tv_step_channel': {'command': 'tv_step_channel',
                     'comment': 'MPlayer command: tv_step_channel Integer',
                     'pycommand': 'tv_step_channel(<int>)',
                     'types': ['int']},
 'tv_step_freq': {'command': 'tv_step_freq',
                  'comment': 'MPlayer command: tv_step_freq Float',
                  'pycommand': 'tv_step_freq(<float>)',
                  'types': ['float']},
 'tv_step_norm': {'command': 'tv_step_norm',
                  'comment': 'MPlayer command: tv_step_norm',
                  'pycommand': 'tv_step_norm()',
                  'types': []},
 'use_master': {'command': 'use_master',
                'comment': 'MPlayer command: use_master',
                'pycommand': 'use_master()',
                'types': []},
 'vo_border': {'command': 'vo_border',
               'comment': 'MPlayer command: vo_border [Integer]',
               'pycommand': 'vo_border([, <int>])',
               'types': ['int']},
 'vo_fullscreen': {'command': 'vo_fullscreen',
                   'comment': 'MPlayer command: vo_fullscreen [Integer]',
                   'pycommand': 'vo_fullscreen([, <int>])',
                   'types': ['int']},
 'vo_ontop': {'command': 'vo_ontop',
              'comment': 'MPlayer command: vo_ontop [Integer]',
              'pycommand': 'vo_ontop([, <int>])',
              'types': ['int']},
 'vo_rootwin': {'command': 'vo_rootwin',
                'comment': 'MPlayer command: vo_rootwin [Integer]',
                'pycommand': 'vo_rootwin([, <int>])',
                'types': ['int']},
 'vobsub_lang': {'command': 'vobsub_lang',
                 'comment': 'MPlayer command: vobsub_lang [Integer]',
                 'pycommand': 'vobsub_lang([, <int>])',
                 'types': ['int']},
 'volume': {'command': 'volume',
            'comment': 'MPlayer command: volume Float [Integer]',
            'pycommand': 'volume(<float>[, <int>])',
            'types': ['float', 'int']}}