<template>
    <v-container class="d-flex flex-column align-center justify-center">
        <h1>Users</h1>
        <div>
            <UserCreation />
            <UserList />
        </div>
    </v-container>
</template>

<script>
import UserCreation from '../components/UserCreation.vue';
import UserList from '../components/UserList.vue';

export default {
    components: {
        UserCreation,
        UserList,
    },
};
</script>