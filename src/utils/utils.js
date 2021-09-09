const mixin = {
    methods: {
        goTo(path) {
            this.$router.push(path);
        }
    }
};

export default mixin;