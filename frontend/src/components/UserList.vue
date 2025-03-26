<template>
    <v-list>
        <v-list-item v-for="user in users" :key="user.id">
            <v-list-item-title class="d-flex justify-space-between align-center">
                {{ user.username }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ user.borrows.length }} borrow(s)</v-list-item-subtitle>
        </v-list-item>
    </v-list>
</template>

<script>
export default {
    data() {
        return {
            users: []
        };
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await fetch('http://localhost:4000/users');
                if (!response.ok) throw new Error("Error fetching users");
                const data = await response.json();
                this.users = data.users;
            } catch (error) {
                console.error("fetch users failed:", error);
                this.users = [];
            }
        },
    },
    mounted() {
        this.fetchUsers();
    }
};
</script>