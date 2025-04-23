// Styles
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import { aliases, md } from 'vuetify/iconsets/md'
import 'vuetify/styles'

// Vuetify
import { createVuetify } from 'vuetify'

export default createVuetify({
    icons: {
        defaultSet: 'md',
        aliases,
        sets: {
          md,
        },
    },
});
