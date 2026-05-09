TAG_STRINGS = ["favourite", "wanted", "digital", "physical"]
ACTIVE_TAG_ICONS = ["favorite", "star", "audio_file", "album"]
DISABLED_TAG_ICONS = ["favorite_border",
                      "star_border", "o_audio_file", "o_album"]


def get_tag_states(tags) -> list[bool]:
    tag_states: list[bool] = [
        False for _ in range(len(TAG_STRINGS))
    ]
    for tag in tags.json():
        tag_states[TAG_STRINGS.index(tag["tag"])] = True

    return tag_states
